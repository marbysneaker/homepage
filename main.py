import utils
import sys    




    

        
if __name__ == "__main__":
    print("this is argv: ", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == 'build':
        print("build was specified")
        utils.create_pages()
        utils.render()
    elif command == 'new':
        print("New page was specified")
        open(utils.new_content['page'],"w+").write(utils.new_content['content'])
    else:
        print("Please specify build or new")
            