import os,shutil

# Paper folder organize

folder_path = "Paper/"

archive_list = os.listdir(folder_path+"Archive")

for pdf_file in archive_list:
    if pdf_file [-4:] != ".pdf":
        print("File type not recognised: %s"%pdf_file)

    # read pdf name
    pdf_name = pdf_file[:-4]
    print("Detect PDF file: %s"%pdf_file)

    # get_folder_name
    folder_name = "_".join(pdf_name.lower().split(" "))
    print("Create folder: %s"%folder_name)

    # create folder, move pdf file
    if os.path.exists(folder_path+folder_name):
        pass
    else:
        os.mkdir(folder_path+folder_name)
    shutil.move(folder_path+"Archive/"+pdf_file,folder_path+folder_name)

    # create markdown file
    f = open(folder_path+folder_name+"/papernote.md","w")
    f.close()


# Generate paper content
collect_list = os.listdir(folder_path)
f = open(folder_path+"index.md","w")
f.write("# Paper\n\n")
for paper_item in collect_list:
    if paper_item == "Archive" or paper_item == "index.md":
        pass
    else:
        f.write("- [%s](./%s/papernote.md)\n\n"%(" ".join(paper_item.split("_")),paper_item))
f.close()






