import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage
import gzip
import json

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection('document_Reference')


client = storage.Client.from_service_account_json('../example')
bucket = client.get_bucket('Bucket')
table=[]


#insert decompressed file as firestore data
def list_blobs(bucket_name):
	blobs = client.list_blobs(bucket_name)
	for blob in blobs:
		print(blob.name)
		blobFile = bucket.get_blob(blob.name)
		blobString = blobFile.download_as_string()
		data = json.loads(gzip.decompress(blobString))
		
		
		doc_ref.document(str(blob)).set({
			'child1':str(data['value1'][str(x)]),
			'child2':str(data['value2'][str(x)]),
		})


list_blobs('bucket_name');

#terminal shows content in file
'''with gzip.GzipFile(blob, 'r') as fin:   
        	for line in fin:
        		table.append(json.loads(line))
        for row in table:
        	print(row)'''

blobFile = bucket.get_blob('MyFile.json.gz')
blobString = blobFile.download_as_string()
print(finished)
