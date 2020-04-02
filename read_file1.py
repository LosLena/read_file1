cook_book = {}
list_data = []
file_path = 'recipes.txt'
with open(file_path, encoding='utf8') as file_data:
    for line in file_data:
        #del list_data[:]
        #print(line)
        name_bluda = line.strip()
        kol_vo = int(file_data.readline().strip())
        if not name_bluda:
            break
        #print(name_bluda, kol_vo)
        list_data = []
        for number in range(int(kol_vo)):
          ingredient_name = file_data.readline().strip().split("|")
          #print(ingredient_name)
          #print(ingredient_name[0])
          list_data.append({'ingredient_name': ingredient_name[0].strip(), 'quantity': ingredient_name[1].strip(), 'measure': ingredient_name[2].strip()})
          cook_book[name_bluda] =  list_data
          #print(list_data)
          #print (type(number))
        file_data.readline()
          
        #file_data.readline()    
           

for bludas, ingredients in cook_book.items():
    print(bludas, ingredients)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
      for ingridient in cook_book[dish]:
        new_shop_list_item = dict(ingridient)
        key = new_shop_list_item["ingredient_name"]
        #print(key)
        list_data = []
        availability_key = shop_list.get(key)
        if availability_key  == None:
          list_data.append({'measure': new_shop_list_item["measure"], 'quantity':int(new_shop_list_item["quantity"])* person_count})
          #print(list_data)
          shop_list[key] = list_data 
        else:
           #kkk = key
           kkk1= shop_list[key][0]["quantity"]
           #print(key, kkk1)
           shop_list[key][0]["quantity"] += int(new_shop_list_item['quantity'])* person_count
           # здесь опять запуталась
                  
                  
   
    
    print(shop_list)
           
  

  
print("====================================")
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

