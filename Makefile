nmon:
	./bin/nmon -f -s 1 -c 30 -m dist/nmon; \
	/usr/bin/ansible -i inventory all -a "/root/gateway-test/bin/nmon -f -s 1 -c 30 -m /root/gateway-test/dist/nmon/" -u root --become-user root

chart:
	./bin/chart dist/nmon/$$(hostname)_$$(date +%y%m%d_%H%M).nmon dist/$$(date +%y%m%d_%H%M).html

wrk100: nmon
	name=$$(hostname)_$$(date +%y%m%d_%H%M).nmon ; \
	./bin/wrk -t4 -c100 -d30s http://10.116.18.230:8081/app/abc > wrk-log/c100.log; \
	python ./bin/excel.py ./result.xls wrk-log/c100.log 100; \
	./bin/chart dist/nmon/$$name dist/c100.html

wrk200:
	./bin/wrk -t4 -c200 -d30s http://10.116.18.230:8081/app/abc > wrk-log/c200.log; \
	python ./bin/excel.py ./result.xls wrk-log/c200.log 200
