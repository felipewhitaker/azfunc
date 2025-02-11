import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="sample-workitems",
                               connection="4931ba_STORAGE") 
def blob_triggered(myblob: func.InputStream):
    # is triggered both for new blobs in `sample-workitems` and
    #   `sample-workitems/temp`
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

@app.blob_trigger(arg_name="myblob", path="sample-workitems/temp",
                               connection="4931ba_STORAGE") 
def temp_triggered(myblob: func.InputStream):
    # is not triggered when a blob enters `sample-workitems/temp`
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")