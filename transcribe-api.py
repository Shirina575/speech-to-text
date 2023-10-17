import requests
import json

import time
import boto3
import urllib.request


def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                transcript_url = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
                response = urllib.request.urlopen(transcript_url)
                data = json.loads(response.read())
                print(data["results"]['transcripts'][0]['transcript'])
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def main():
    transcribe_client = boto3.client('transcribe')
    file_uri = 's3://test-transcribe/answer2.wav'
    transcribe_file(f'Example-job-{time.time()}', file_uri, transcribe_client)


if __name__ == '__main__':
    main()