#python3


import urllib.request
from bs4 import BeautifulSoup

#breaks on no-finds AND on multi-finds (selects wrong person if > 2)
# only works on perfect hits

names = [] #list


def parse(rows):
  """ Get data from rows """
  results = []
  for row in rows:
      table_headers = row.find_all('th')
      if table_headers:
          results.append([headers.get_text() for headers in table_headers])

      table_data = row.find_all('td')
      if table_data:
          results.append([data.get_text() for data in table_data])
  rets = results[1][0]+' <'+results[3][0]+'@virginia.edu>'
  # TODO Handle errors, print/collect bad names
  return rets

def start():
  # print intro message and who wrote program
  # output will be UVAEmails.txt

def check():
  #warn user if uvaemails.txt detected

def inputcsv():
  # prompt for input file (csv of names)
  # turn csv into list of strings
  return li #list

def findemails(names):
  f = open("UVAEmails.txt","w")
  for name in names:
    url = 'http://its.virginia.edu/search/people/?s='+name.replace(' ','+')+'&b=name'
    http = urllib.request.urlopen(url)
    soup = BeautifulSoup(http.read())
    table = soup.find('table')
    rows = table.find_all('tr')
    rows = table.find_all('tr')
    li = parse(rows)
    f.write(li+'\n')
    # print(name)
  f.close()

def end():
  # print outro message.

def main():

  start()
  check()
  names = inputcsv()
  end()

if __name__ == "__main__":
  main()
