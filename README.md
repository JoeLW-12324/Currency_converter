# Currency Converter 

A currency converter GUI app developed with python and tkinter.

This application is created by me to convert currencies by inputting two 
currency codes and clicking the "Convert now" button. 

This application used the Exchange Rates API to receive the converted result and 
users are able to manipulate the output result by inputting a certain amount to be converted,
and set a historical date. 

The user can click on the history button to check their past pairs of currency code converted that are in a 
form of a button in another GUI and they are able to click on one of the buttons to be input the pairs of codes 
into the main GUI again to be used as conversion.

The user can also click on the date checkmark to have a historical rate when converting currencies. The user can also 
click the "Set date" button to set a past date for a historical rate they want in another GUI.  

This app contains a history.txt file to save and track the user past history of any pair of currency they have converted with. 
The pair of currencies code are written as ("from-currency-code"-"to_currency_code") in the txt file. User should not put any other format 
in this txt file or it will break the application. When the user close the main GUI, the program will then write their new history of converted pairs of currency code 
into the txt file. 

This projects imports the tkcalendar and requests modules and you will need to install both of 
these modules to use this GUI application. 