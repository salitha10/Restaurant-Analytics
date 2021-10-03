import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

html_temp = """ 
    <div style ="background-color:yellow;padding:10px"> 
    <h1 style ="color:black;text-align:center;">Predict Rating </h1>
    </div>
    <div style = "margin-bottom:20px"> </div>
    """
# st.markdown(html_temp, unsafe_allow_html = True) 

def app():
    st.markdown(""" # Predict Rating """)
    st.write("Enter details of your restaurent to predict the rating.")

    location_select = st.selectbox('Select the location',['Banashankari', 'Basavanagudi', 'Jayanagar', 'Kumaraswamy Layout',
        'Rajarajeshwari Nagar', 'Mysore Road', 'Uttarahalli',
        'South Bangalore', 'Vijay Nagar', 'Bannerghatta Road', 'JP Nagar',
        'BTM', 'Wilson Garden', 'Koramangala 5th Block', 'Shanti Nagar',
        'Richmond Road', 'City Market', 'Bellandur', 'Sarjapur Road',
        'Marathahalli', 'HSR', 'Old Airport Road', 'Indiranagar',
        'Koramangala 1st Block', 'East Bangalore', 'MG Road',
        'Brigade Road', 'Lavelle Road', 'Church Street', 'Ulsoor',
        'Residency Road', 'Shivajinagar', 'Infantry Road',
        'St. Marks Road', 'Cunningham Road', 'Race Course Road', 'Domlur',
        'Koramangala 8th Block', 'Frazer Town', 'Ejipura', 'Vasanth Nagar',
        'Jeevan Bhima Nagar', 'Old Madras Road', 'Commercial Street',
        'Koramangala 6th Block', 'Majestic', 'Langford Town',
        'Koramangala 7th Block', 'Brookefield', 'Whitefield',
        'ITPL Main Road, Whitefield', 'Varthur Main Road, Whitefield',
        'Koramangala 2nd Block', 'Koramangala 3rd Block',
        'Koramangala 4th Block', 'Koramangala', 'Bommanahalli',
        'Hosur Road', 'Seshadripuram', 'Electronic City', 'Banaswadi',
        'North Bangalore', 'RT Nagar', 'Kammanahalli', 'Hennur',
        'HBR Layout', 'Kalyan Nagar', 'Thippasandra', 'CV Raman Nagar',
        'Kaggadasapura', 'Kanakapura Road', 'Nagawara', 'Rammurthy Nagar',
        'Sankey Road', 'Central Bangalore', 'Malleshwaram',
        'Sadashiv Nagar', 'Basaveshwara Nagar', 'Rajajinagar',
        'New BEL Road', 'West Bangalore', 'Yeshwantpur', 'Sanjay Nagar',
        'Sahakara Nagar', 'Jalahalli', 'Yelahanka', 'Magadi Road',
        'KR Puram'])

    locations = {'Banashankari': 1,
    'Basavanagudi': 4,
    'Jayanagar': 30,
    'Kumaraswamy Layout': 46,
    'Rajarajeshwari Nagar': 63,
    'Mysore Road': 54,
    'Uttarahalli': 79,
    'South Bangalore': 75,
    'Vijay Nagar': 82,
    'Bannerghatta Road': 3,
    'JP Nagar': 28,
    'BTM': 0,
    'Wilson Garden': 85,
    'Koramangala 5th Block': 42,
    'Shanti Nagar': 73,
    'Richmond Road': 66,
    'City Market': 13,
    'Bellandur': 6,
    'Sarjapur Road': 71,
    'Marathahalli': 53,
    'HSR': 22,
    'Old Airport Road': 58,
    'Indiranagar': 26,
    'Koramangala 1st Block': 38,
    'East Bangalore': 17,
    'MG Road': 49,
    'Brigade Road': 8,
    'Lavelle Road': 48,
    'Church Street': 12,
    'Ulsoor': 78,
    'Residency Road': 65,
    'Shivajinagar': 74,
    'Infantry Road': 27,
    'St. Marks Road': 76,
    'Cunningham Road': 15,
    'Race Course Road': 61,
    'Domlur': 16,
    'Koramangala 8th Block': 45,
    'Frazer Town': 20,
    'Ejipura': 18,
    'Vasanth Nagar': 81,
    'Jeevan Bhima Nagar': 31,
    'Old Madras Road': 59,
    'Commercial Street': 14,
    'Koramangala 6th Block': 43,
    'Majestic': 51,
    'Langford Town': 47,
    'Koramangala 7th Block': 44,
    'Brookefield': 9,
    'Whitefield': 84,
    'ITPL Main Road, Whitefield': 25,
    'Varthur Main Road, Whitefield': 80,
    'Koramangala 2nd Block': 39,
    'Koramangala 3rd Block': 40,
    'Koramangala 4th Block': 41,
    'Koramangala': 37,
    'Bommanahalli': 7,
    'Hosur Road': 24,
    'Seshadripuram': 72,
    'Electronic City': 19,
    'Banaswadi': 2,
    'North Bangalore': 57,
    'RT Nagar': 60,
    'Kammanahalli': 35,
    'Hennur': 23,
    'HBR Layout': 21,
    'Kalyan Nagar': 34,
    'Thippasandra': 77,
    'CV Raman Nagar': 10,
    'Kaggadasapura': 33,
    'Kanakapura Road': 36,
    'Nagawara': 55,
    'Rammurthy Nagar': 64,
    'Sankey Road': 70,
    'Central Bangalore': 11,
    'Malleshwaram': 52,
    'Sadashiv Nagar': 67,
    'Basaveshwara Nagar': 5,
    'Rajajinagar': 62,
    'New BEL Road': 56,
    'West Bangalore': 83,
    'Yeshwantpur': 87,
    'Sanjay Nagar': 69,
    'Sahakara Nagar': 68,
    'Jalahalli': 29,
    'Yelahanka': 86,
    'Magadi Road': 50,
    'KR Puram': 32}


    location = locations[location_select]


    cuisine_select = st.multiselect('Select the cuisines',['North Indian',
    'Chinese',
    'Continental',
    'Cafe',
    'Fast Food',
    'South Indian',
    'Italian',
    'Desserts',
    'Biryani',
    'Beverages'])

    if 'North Indian' in cuisine_select:
        North_Indian = 1
    else:
        North_Indian = 0
    if 'Chinese' in cuisine_select:
        Chinese = 1
    else:
        Chinese = 0
    if 'Continental' in cuisine_select:
        Continental = 1
    else:
        Continental = 0
    if 'Cafe' in cuisine_select:
        Cafe = 1
    else:
        Cafe = 0
    if 'Fast Food' in cuisine_select:
        Fast_Food = 1
    else:
        Fast_Food = 0
    if 'South Indian' in cuisine_select:
        South_Indian = 1
    else:
        South_Indian = 0
    if 'Italian' in cuisine_select:
        Italian = 1
    else:
        Italian = 0
    if 'Desserts' in cuisine_select:
        Desserts = 1
    else:
        Desserts = 0
    if 'Biryani' in cuisine_select:
        Biryani = 1
    else:
        Biryani = 0
    if 'Beverages' in cuisine_select:
        Beverages = 1
    else:
        Beverages = 0


    rest_type_select = st.multiselect('Select the restaurent type',
    ['Bakery', 'Bar', 'Beverage Shop', 'Cafe', 'Casual Dining', 'Club',
        'Delivery', 'Dessert Parlor', 'Dhaba', 'Fine Dining', 'Food Court',
        'Food Truck', 'Irani Cafee', 'Kiosk', 'Lounge', 'Mess', 'Microbrewery',
        'Pub', 'Quick Bites', 'Sweet Shop', 'Takeaway'])

    if 'Bakery' in rest_type_select:
        Bakery = 1
    else:
        Bakery = 0
    if 'Bar' in rest_type_select:
        Bar = 1
    else:
        Bar = 0
    if 'Beverage Shop' in rest_type_select:
        Beverage_Shop = 1
    else:
        Beverage_Shop = 0
    if 'Cafe' in rest_type_select:
        Cafe = 1
    else:
        Cafe = 0
    if 'Casual Dining' in rest_type_select:
        Casual_Dining = 1
    else:
        Casual_Dining = 0
    if 'Club' in rest_type_select:
        Club = 1
    else:
        Club = 0
    if 'Delivery' in rest_type_select:
        Delivery = 1
    else:
        Delivery = 0
    if 'Dessert Parlor' in rest_type_select:
        Dessert_Parlor = 1
    else:
        Dessert_Parlor = 0
    if 'Dhaba' in rest_type_select:
        Dhaba = 1
    else:
        Dhaba = 0
    if 'Fine Dining' in rest_type_select:
        Fine_Dining = 1
    else:
        Fine_Dining = 0
    if 'Food Court' in rest_type_select:
        Food_Court = 1
    else:
        Food_Court = 0
    if 'Food Truck' in rest_type_select:
        Food_Truck = 1
    else:
        Food_Truck = 0
    if 'Irani Cafee' in rest_type_select:
        Irani_Cafee = 1
    else:
        Irani_Cafee = 0
    if 'Kiosk' in rest_type_select:
        Kiosk = 1
    else:
        Kiosk = 0
    if 'Lounge' in rest_type_select:
        Lounge = 1
    else:
        Lounge = 0
    if 'Mess' in rest_type_select:
        Mess = 1
    else:
        Mess = 0
    if 'Microbrewery' in rest_type_select:
        Microbrewery = 1
    else:
        Microbrewery = 0
    if 'Pub' in rest_type_select:
        Pub = 1
    else:
        Pub = 0
    if 'Quick Bites' in rest_type_select:
        Quick_Bites = 1
    else:
        Quick_Bites = 0
    if 'Sweet Shop' in rest_type_select:
        Sweet_Shop = 1
    else:
        Sweet_Shop = 0
    if 'Takeaway' in rest_type_select:
        Takeaway = 1
    else:
        Takeaway = 0


    listed_in_select = st.selectbox('Service type', ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
        'Drinks & nightlife', 'Pubs and bars'])

    listed_ins = {'Buffet': 0,
    'Cafes': 1,
    'Delivery': 2,
    'Desserts': 3,
    'Dine-out': 4,
    'Drinks & nightlife': 5,
    'Pubs and bars': 6}

    listed_in = listed_ins[listed_in_select]

    cost_for_two = st.number_input('Cost for two', min_value=0, max_value=10000)

    st.write('Facilities provided')
    online_order = st.checkbox('Online Order');
    book_table = st.checkbox('Table booking');

    votes = 604.38

    submit = st.button('Predict Rating')

    if submit:

        if not cuisine_select or not rest_type_select or cost_for_two == 0:
            st.error('Please fill all the fields')
        else:
            result = classifier.predict([[online_order, book_table, votes, location, cost_for_two, listed_in,
                Beverages, Biryani, Cafe, Chinese, Continental, Desserts,
                Fast_Food, Italian, North_Indian, South_Indian, Bakery, Bar,
                Beverage_Shop, Cafe, Casual_Dining, Club, Delivery,
                Dessert_Parlor, Dhaba, Fine_Dining, Food_Court, Food_Truck,
                Irani_Cafee, Kiosk, Lounge, Mess, Microbrewery, Pub,
                Quick_Bites, Sweet_Shop, Takeaway]])

            st.success('Preidcted rating is {}'.format(str(result).strip()[1:-1]))

