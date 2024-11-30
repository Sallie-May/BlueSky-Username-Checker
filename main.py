import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored 

def resolve_handle(handle):
    handle = handle.strip() 
    handle = handle + ".bsky.social"
    handle = handle.lower()
    url = f"https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle={handle}"

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr-FR, fr;q=0.9, en-US;q=0.8, en;q=0.7",
        "atproto-accept-labelers": "did:plc:ar7c4by46qjdydhdevvrndac;redact",
        "cache-control": "no-cache",
        "dnt": "1",
        "origin": "https://bsky.app",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://bsky.app/",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    valid_handles = []

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(colored(f"{handle} ALREADY TAKEN!", 'red')) 
        else:
            print(colored(f"{handle} IS VALID", 'green')) 
            valid_handles.append(handle) 
            
    except requests.exceptions.RequestException as e:
        print(colored(f"Error resolving handle {handle}: {e}", 'yellow'))  

    return valid_handles 

def process_handles_from_file(input_file, num_threads):
    with open(input_file, 'r') as file:
        handles = file.readlines()
    
    all_valid_handles = []  
    
    # Use ThreadPoolExecutor to run in parallel
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(resolve_handle, handle) for handle in handles]
        
        for future in futures:
            all_valid_handles.extend(future.result())

    return all_valid_handles  

def write_valid_handles(output_file, valid_handles):
    with open(output_file, 'w') as file:
        for handle in valid_handles:
            file.write(handle + "\n")

def main(input_file, output_file, num_threads):
    valid_handles = process_handles_from_file(input_file, num_threads)  
    write_valid_handles(output_file, valid_handles)  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolve handle availability on Bluesky.")
    parser.add_argument("input_file", nargs='?', default="handles.txt", help="Input file with handles to check (default: handles.txt).")
    parser.add_argument("output_file", nargs='?', default="valid_handles.txt", help="Output file for valid handles (default: valid_handles.txt).")
    parser.add_argument("-t", "--threads", type=int, default=None, help="Number of threads to use (default: 20).")

    args = parser.parse_args()

    if not args.threads:
        try:
            args.threads = int(input("Please enter the number of threads (default 20): "))
        except ValueError:
            args.threads = 20 

    main(args.input_file, args.output_file, args.threads)
