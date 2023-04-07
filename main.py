
import analysis


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
    

def main():

    display_menu()
    while True:
        choice = input("Enter choice (Press x to exit): ")
        if (choice == "1"):
         analysis.create_summary_file()
         print("Completed! File saved in 'data' folder!")
        elif (choice == "2"):
         analysis.plot_petal_length_hist()
         analysis.plot_petal_width_hist()
         analysis.plot_sepal_length_hist()
         analysis.plot_sepal_width_hist()
         print("Completed! Histograms saved in 'images' folder!")  
        elif (choice == "3"):
         analysis.plot_sepal_scattor()
         analysis.plot_petal_scattor()
         print("Completed! ScattorPlots saved in 'images' folder!") 
        elif (choice == "4"):
         analysis.boxplots()
         print("Completed! BoxPlots saved in 'images' folder!")
        elif (choice == "5"):
         analysis.pairplot()
         print("Completed! BoxPlots saved in 'images' folder!") 
        elif (choice in ("x",'X')):
           print('Goodbye!')
           break
        else :
           display_menu()



if __name__ == "__main__":
    main()