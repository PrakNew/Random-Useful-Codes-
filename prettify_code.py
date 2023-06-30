import pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(mydict)

import json
print(json.dumps(mydict,sort_keys=True,indent=4))
