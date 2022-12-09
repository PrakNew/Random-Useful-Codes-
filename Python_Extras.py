#Creating and activating virtual environment
pip install virtualenv
virtualenv foo
cd .\foo
.\Scripts\activate

#Creating and installing from requirements.txt file
pip freeze > requirements.txt
pip install -r requirements.txt

# Commmand line
python -m http.server

l=[]
for x in range(5):
  l+=x,  #behaves like append
  
vars(Object/Class) -> return a dictionary
