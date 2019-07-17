# -*- coding: utf-8 -*-
import sys
import xlwt
import xlrd
import xlutils.copy
import re

"""
xlutils 仅支持xls格式，不支持xlsx
"""

class Report:
   """
   """
   def __init__(self):
      self.column  = {
         '100':2,
         '200':3,
         '300':4,
         '400':5
      }
      pass
   # end def __init__

   def fill(self, filename, wrk):
      """
      填充文档内容
      """
      rb = xlrd.open_workbook(filename) 
      workbook = xlutils.copy.copy(rb)
      sheet = workbook.get_sheet(1)
      #sheet.write(0,0,'Hi changei!!')
      sheet.write(7, self.column[wrk.concurrency], wrk.latency_avg)
      sheet.write(8, self.column[wrk.concurrency], wrk.qps_avg)
      sheet.write(9, self.column[wrk.concurrency], wrk.tps)
      sheet.write(10,self.column[wrk.concurrency], wrk.qps)
      sheet.write(11,self.column[wrk.concurrency], wrk.request_count)
      sheet.write(12,self.column[wrk.concurrency], wrk.response_count)
      
      workbook.save(filename)

   #end def test


class WrkReport:
   """
   Running 30s test @ http://10.116.18.230:8081/app/abc
   4 threads and 10 connections
   Thread Stats   Avg      Stdev     Max   +/- Stdev
      Latency   254.14us  133.58us   7.39ms   95.95%
      Req/Sec     7.96k   458.58     9.12k    76.00%
   954295 requests in 30.10s, 66.61MB read
   Non-2xx or 3xx responses: 954295
   Requests/sec:  31704.26
   Transfer/sec:      2.21MB   
   """

   def __init__(self):
      self.concurrency= '100'
      pass
   # end def __init__

   def parse(self, filename):
      with open(filename,'r') as f:
         lines = f.readlines()
         latency = re.split('\\s+', lines[3].strip())
         tps = re.split('\\s+', lines[4].strip())
         requests = re.split('\\s+', lines[5].strip())
         responses= re.split('\\s+', lines[6].strip())
         qps = re.split('\\s+', lines[7].strip())
         tpstotlal = re.split('\\s+', lines[8].strip())
         self.latency_avg = latency[1]
         self.qps_avg = tps[1]
         self.qps = qps[1]
         self.tps = tpstotlal[1]
         self.request_count = requests[0]
         self.response_count = responses[-1:]
   #end def parse


def main():
   """
   python excel.py ./1.xls ./wrk.log 100
   """
   report = Report()
   filename = sys.argv[1]
   
   wrk = WrkReport()
   wrk.parse( sys.argv[2])

   wrk.concurrency = sys.argv[3]
   report.fill(filename, wrk)
   print('OK')

if __name__ == '__main__':
    main()
