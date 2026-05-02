#!/usr/bin/env python3
"""Generate game sound effects via ElevenLabs Sound Effects API"""
import requests
import os
import json

API_KEY = os.environ.get('ELEVENLABS_API_KEY')
BASE_URL = 'https://api.elevenlabs.io/v1/sound-generation'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

effects = [
    {
        'name': 'sfx-knight-walk',
        'prompt': 'Heavy armored knight walking, metal boots on dirt, clanking armor, rhythmic steps, medieval',
        'duration': 0.5,
    },
    {
        'name': 'sfx-knight-jump',
        'prompt': 'Knight jumping upward with heavy armor, whoosh, metal clank, energetic leap',
        'duration': 0.6,
    },
    {
        'name': 'sfx-knight-attack',
        'prompt': 'Sword slash, metal blade swinging through air, sharp whoosh, medieval weapon attack, powerful strike',
        'duration': 0.8,
    },
    {
        'name': 'sfx-pig-walk',
        'prompt': 'Pig trotting on dirt, small hooves clopping, soft rhythmic animal footsteps',
        'duration': 0.4,
    },
    {
        'name': 'sfx-pig-stunned',
        'prompt': 'Cartoon hit impact, thud, boing, character getting dazed, dizzy sound effect',
        'duration': 0.6,
    },
    {
        'name': 'sfx-pig-die',
        'prompt': 'Cartoon pig defeat, squeal, poof, puff of smoke, comedic death sound effect',
        'duration': 1.0,
    },
]

headers = {
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'audio/mpeg',
}

for fx in effects:
    print(f"Generating {fx['name']}...")
    payload = {
        'text': fx['prompt'],
        'duration_seconds': fx['duration'],
        'prompt_influence': 0.3,
        'output_format': 'mp3_44100_128',
    }
    
    resp = requests.post(BASE_URL, headers=headers, json=payload)
    
    if resp.status_code == 200:
        path = os.path.join(OUT_DIR, f"{fx['name']}.mp3")
        with open(path, 'wb') as f:
            f.write(resp.content)
        print(f"  ✓ Saved {path} ({len(resp.content)} bytes)")
    else:
        print(f"  ✗ Error {resp.status_code}: {resp.text[:200]}")

print("\nDone!")
