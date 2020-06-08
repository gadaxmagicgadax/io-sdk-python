import requests
import json
# import pandas as pd

# SELECT 								  0 AS amount,
#                                         scadenza AS due_date,
#                                         destinatario AS fiscal_code,
#                                         false AS invalid_after_due_date,
#                                         testo AS markdown,
#                                         1 AS notice_number,
#                                         titolo AS subject FROM messages

def main(args):

	import config
	
	query = """query {
    data : messages {
		due_date : scadenza
		fiscal_code : destinatario
		markdown : testo
		subject : titolo
  		}
	}"""

	# url = args.get("url") if args.get("url") else 'http://172.17.0.1:8080/v1/graphql'
	if args.get("url") == None:
		print(config.emptyForm)
		json_data = json.loads(config.emptyForm)
		print(json_data)
		return {"body": json_data}

	try:
		r = requests.post(args.get("url"), json={'query': query})
	except requests.exceptions.RequestException as e:
		print(e)
		#json_data = json.loads(str(e))
		#print(json_data)
		return {"body": str(e)}

	json_data = json.loads(r.text)

	# parse json_data to add fixed fields (should be made by the query?)	
	for item in json_data['data']['data']:
    		item.update(amount = 0, invalid_after_due_data = False, notice_number = 1)
	print(json_data)
	return {"body": json_data['data']}
