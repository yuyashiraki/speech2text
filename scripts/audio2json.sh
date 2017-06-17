#!/bin/sh

if [ $# -ne 3 ]; then
  exit 1
fi

cd $(dirname $0)/../mnt

export AUDIO_FILE=$PWD/$1
export JSON_FILE=$PWD/$2
export AUDIO_WAV=$(cut $audio_file -d'.' -f1).wav
export LANG=$3

sox $audio_file $audio_wav channels 1 rate 16k

cat > $json_file <<EOF
{
    "config": {
        "languageCode" : "$lang"
    },
    "audio": {
        "content" : $(base64 $audio_wav)
    }
}
EOF

exit 0
