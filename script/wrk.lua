done = function(summary, latency, requests)
	local errors=0
        for key,val in pairs(summary.errors) do 
		print(key..":"..val)
		errors = errors+val
	end
	print("requests successfully="..summary.requests-errors)
	print("requests failed="..errors )
end
init = function(arg)
	wrk.headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb2RlIjoiYWRtaW4iLCJpcCI6IjEwLjExNi4xOC43MSIsInJvbGVDb2RlcyI6ImFkbWluIiwibWFjIjpudWxsLCJjb21wYW55SWQiOjEsInJvbGVJZHMiOiIxIiwibG9naW5UaW1lIjoxNTYwOTExMTExNDU2LCJsb2dpbk5hbWUiOiJhZG1pbiIsIm5hbWUiOiJZV1J0YVc0PSIsImlkIjoxLCJleHAiOjE1NjA5OTc1MTE0NTcsInJvbGVOYW1lcyI6Iui2hee6p-euoeeQhuWRmCJ9.MmKhPq_5FKqD7qZsLaUHvChB_ZegaDDqeHLsX_RIdIY"
end
	
