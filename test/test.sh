. ~/.searchdisplay.env.sh
curl -X POST http://127.0.0.1:7900/api/upload_document \
  -H "Authorization: Token ${WEBSERVICE_API_TOKEN}" \
  -F "file=@$HOME/tmp/hill.jpg" \
  -F "converted_text=Another record for the hill $(date '+%Y%m%d-%H%M%s')."