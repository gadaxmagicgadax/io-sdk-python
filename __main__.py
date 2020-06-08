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
	query = """query {
    messages {
		due_date : scadenza
		fiscal_code : destinatario
		markdown : testo
		subject : titolo
  		}
	}"""

	url = args.get("url") if args.get("url") else 'http://172.17.0.1:8080/v1/graphql'
 	
	r = requests.post(url, json={'query': query})
	print(r.status_code)
	print(r.text)
	print(type(r.text))
	json_data = json.loads(r.text)
	print(json_data)
	return {"body": json_data}