if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BalamuruganDV/Uchiha-itachi.git /Uchiha-itachi
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Uchiha-itachi
fi
cd /Uchiha-itachi
pip3 install -U -r requirements.txt
echo "𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝚄𝚌𝚑𝚒𝚑𝚊..."
python3 bot.py
