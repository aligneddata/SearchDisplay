#!/bin/bash

# Set the API token and URL
. ~/.searchdisplay.env.sh
API_TOKEN="${WEBSERVICE_API_TOKEN}"  # Replace with your actual token
API_URL="http://127.0.0.1:7900/api/upload_document_and_text"

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <document_file> <text_file>"
  exit 1
fi

# Get the filenames from the command-line arguments, handling spaces
document_file="$1"
text_file="$2"

# Check if the files exist
if [ ! -f "$document_file" ]; then
  echo "Error: Document file '$document_file' not found."
  exit 1
fi

if [ ! -f "$text_file" ]; then
  echo "Error: Text file '$text_file' not found."
  exit 1
fi

# Construct the curl command using variables and proper quoting
curl_command=(
  curl
  -X POST
  -H "Authorization: Token $API_TOKEN"
  -F "file=@$document_file"
  -F "text=@$text_file"
  "$API_URL"
)

# Execute the curl command
"${curl_command[@]}"

# Check the exit status of the curl command
ret=$?
if [ $ret -eq 0 ]; then
  echo "File upload successful."
else
  echo "File upload failed."
fi

exit $ret