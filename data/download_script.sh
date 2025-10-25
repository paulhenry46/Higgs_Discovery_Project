RECORDS="12362 12363 12364 12365 12366 12367 12368"

# Loop through each Record ID and run the download command
for ID in $RECORDS; do
    echo "Starting download for Record ID: $ID"
    
    # Optional: Use XRootD protocol for potentially better performance
    cernopendata-client download-files --recid $ID #--protocol xrootd 
    
    echo "Finished download for Record ID: $ID"
    echo "-------------------------------------"
done

echo "All specified records have been processed."