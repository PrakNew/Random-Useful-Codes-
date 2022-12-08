#Creating and activating virtual environment
pip install virtualenv
virtualenv foo
cd .\foo
.\Scripts\activate

# Commmand line
python -m http.server

l=[]
for x in range(5):
  l+=x,  #behaves like append
  
vars(Object/Class) -> return a dictionary
