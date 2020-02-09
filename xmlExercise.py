# Extracting attributes from the xml
import xml.etree.ElementTree as ET

data = """
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>"""
tree = ET.fromstring(data)
print("Name::", tree.find("name").text)
print("Attr::", tree.find("email").get("hide"))

input = """
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>"""

stuff = ET.fromstring(input)
lst = stuff.findall("users/user")
print("User Count ::", len(lst))

count = 1
for loop in lst:
    print("Name ", count, " :", loop.find("name").text)
    print("Id ", loop.find("id").text)
    print("Attribute", loop.get("x"))
    count += 1
