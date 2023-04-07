
import analysis

#Menu for users to view options
def display_menu():
    print("")
    print("-------------------")
    print("Iris Data Set Analysis")
    print("-------------------")
    print("")
    print("MENU")
    print("===============================")
    print("1 - Create Summary File")
    print("2 - Show Histograms")
    print("3 - Show Scattor Plots")
    print("4 - Show Box Plots")
    print("5 - Show Pair Plot")
    print("x - Exit Application")
    

#Main function to start application and display menu
def main():

   #Function to run the menu 
    display_menu()
    while True:
      #Prompt for users to slect options
        choice = input("Enter choice (Press x to exit): ")

        #Option to create summary file
        if (choice == "1"):
         analysis.create_summary_file()
         print("Completed! File saved in 'data' folder!")

         #Option to display and save Histogram images
        elif (choice == "2"):
         analysis.plot_petal_length_hist()
         analysis.plot_petal_width_hist()
         analysis.plot_sepal_length_hist()
         analysis.plot_sepal_width_hist()
         print("Completed! Histograms saved in 'images' folder!")  

        #Option to display and save Scattor Plot images
        elif (choice == "3"):
         analysis.plot_sepal_scattor()
         analysis.plot_petal_scattor()
         print("Completed! ScattorPlots saved in 'images' folder!") 

        #Option to display and save Box Plots images
        elif (choice == "4"):
         analysis.boxplots()
         print("Completed! BoxPlots saved in 'images' folder!")

        #Option to display and save Pair Plot images 
        elif (choice == "5"):
         analysis.pairplot()
         print("Completed! Pair Plots saved in 'images' folder!")

        #Option to exit application. Use can use x or X to exit. 
        elif (choice in ("x",'X')):
           print('Goodbye!')
           break
        
        #If user selects anything excpt options above, menu will run again and prompt user
        else :
           display_menu()


#Run main function
if __name__ == "__main__":
    main()