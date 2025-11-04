echo "starting build"

python -m venv venv
source venv/Scripts/activate

pip install Flask

python3 main.py


echo 
echo
echo "python file has been executed"