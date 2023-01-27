# Bunting Python SDK

Bunting Lab's Python SDK allows you to use the [Bunting Labs geospatial APIs](https://docs.buntinglabs.com/introduction) in your own libraries.

### Installation

```sh
$ pip install bunting
```

### Example

```py
import BuntingClient from bunting

# Get your API key from https://buntinglabs.com/account/register
bc = BuntingClient('gK6vkrFQXiU9')

# Download from openstreetmap
highways = bc.osm.extract('leisure=park', bbox=(5.976563,52.449314,6.245728,52.562995))

# Get as GeoDataFrame
highways.as_gdf()
```
