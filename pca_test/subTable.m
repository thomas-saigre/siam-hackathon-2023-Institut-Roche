clear;
sourceInfo = (input("Source data:","s"));
sytheticInfo = (input("New data:","s"));

sourceTab = (csvReal(sourceInfo));
sythetic = (csvReal(sytheticInfo));

newTable = sourceTab - sythetic;

disp(norm(newTable,Inf))
writematrix((pca(newTable)),"pca_model.csv")
disp(array2table(pca(newTable)))
