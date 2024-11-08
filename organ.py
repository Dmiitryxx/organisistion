import json

organizations=[]
def load_data():
    file=open('organizations.json', 'r')
    data=json.load(file)
    file.close()
    global organizations
    organizations=data['organizations']
    print('DATI PIEVIENOTI')


def add_organization():
        organization_name=input('Organization name: ')
        organization_adress=input('Organization adress: ')
        organization_id=input('Organization id: ')

        organization={
            'name':organization_name,
            'adress':organization_adress,
            'id': organization_id,
             'contacts': []
         }
        while (True):
            response=input('Vai vēlies pievenot kontaktu (jā/nē)')
            if response=='jā':
                print("Darbinrika informācija:")
                contact_name=input('Ievadiet Darbinieka vārdu:')
                contact_position=input('Ievadiet Darbinieka adresse:')
                contact_id=input('Darbinieka id:')
                contact={
                    'name':contact_name,
                    'adress': contact_position,
                    'id': contact_id
                }
                organizations['contacts'].append(contact)
            elif response=='nē':
                break
        organizations.append(organization)

def print_organization():
     for organization in organizations:
            print('---ORGANIZATION---')
            print(f"{organization['name']}({organization['id']})")
            print(f"Adrese:{organization['adress']}")
            print(f"Kontaktu skaits:{len(organization['contacts'])}")

def save_data():
    data={
            'organizations': organizations
        }
    print('SAGLĀBA DATUS.....')
    file=open('organizations.json', 'w')
    json.dump(data, file, indent=4)
    print('Data saved')

def find_organization_by_id():
     organizations_id=input('Ievadiet organizācija ID:')
     for organization in organizations:
          if organization['id']==organization_id:
            print('---ORGANIZATION---')
            print(f"{organization['name']}({organization['id']})")
            break

def main(): 
    load_data()
    while (True):
        response=input('(1) Add organization (2) Print organization (3) Exit')
        if response=='1':
            add_organization()
                
        elif response=='2':
            print_organization()
        elif response=='3':
            save_data()
            print(organizations)
            exit()
        else:
            print("Izvele skaitļu 1,2 vai 3")
            continue
main()