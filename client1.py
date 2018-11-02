from gearman import GearmanClient

new_client = GearmanClient(['www.aispring.top:4730'])
current_request = new_client.submit_job('echo', 'foo')
new_result = current_request.result
print new_result
