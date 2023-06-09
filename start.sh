if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BalamuruganDV/Uchiha-itachi /Uchiha-itachi
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Uchiha-itachi
fi
cd /Luna-latest
pip3 install -U -r requirements.txt
echo "Starting Uchiha❟❛❟...."
python3 bot.py
