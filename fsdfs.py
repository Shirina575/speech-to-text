a = {"jobName":"Example-job","accountId":"636525782246","status":"COMPLETED","results":{"transcripts":[{"transcript":"This is a test."}],"items":[{"type":"pronunciation","alternatives":[{"confidence":"0.999","content":"This"}],"start_time":"0.009","end_time":"0.23"},{"type":"pronunciation","alternatives":[{"confidence":"0.999","content":"is"}],"start_time":"0.239","end_time":"0.389"},{"type":"pronunciation","alternatives":[{"confidence":"0.997","content":"a"}],"start_time":"0.4","end_time":"0.409"},{"type":"pronunciation","alternatives":[{"confidence":"0.999","content":"test"}],"start_time":"0.419","end_time":"1.149"},{"type":"punctuation","alternatives":[{"confidence":"0.0","content":"."}]}]}}
print(a["results"]['transcripts'][0]['transcript'])