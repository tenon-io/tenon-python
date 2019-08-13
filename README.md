### Active maintenance of tenon-python has moved to [tenon-io/tenon-python](https://github.com/tenon-io/tenon-python).

# Python wrapper for the Tenon.io API

## Installation

```shell
pip install tenon-python
```

## Usage

```py
import os
from tenon.api import TenonIO

tenonApi = TenonIO(key=os.environ['TENON_API_KEY'])
response = tenonApi.checkUrl('http://www.example.com')
print(response.text)
```

## Documentation

More information about available options can be found in the [Tenon API documentation](https://bitbucket.org/tenon-io/tenon.io-documentation/src/master/src/2-understanding-api-request-parameters.md).
### `analyze(string, [options])`

Tests a given url, code snippet or full HTML page for accessibility issues.

### `checkUrl(url, [options])`

Tests a given URL for accessibility issues.

### `checkSrc(src, [options])`

Tests a complete HTML document for accessibility issues.

**Note:** if you want to test a fragment, block or snippet of code against Tenon, then use `checkFragment()` or specify `fragment: '1'` in your options.

### `checkFragment(src, [options])`

Tests a fragment, block or snippet of code for accessibility issues.

## Examples

See `examples.py`

## License

Copyright (c) 2015 Justin Stockton  
Licensed under the MIT license.
