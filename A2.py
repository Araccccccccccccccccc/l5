Ammount =int(input("Enter the Ammount for Withdraw: "))

note_1= Ammount//100
note_2= (Ammount%100)//50
note_3= (Ammount%100)%50//20


print("The number of 100  rupee notes is: ", note_1)
print("The number of 50 rupee notes is: ", note_2)
print("The number of 10 rupee notes is: ", note_3)