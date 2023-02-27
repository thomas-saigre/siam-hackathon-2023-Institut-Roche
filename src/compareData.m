clear;
sourceInfo = (input("Source data:","s"));
sytheticInfo = (input("New data:","s"));

sourceTab = array2table(csvReal(sourceInfo));
sythetic = array2table(csvReal(sytheticInfo));

%sourceTab = readtable('source.csv');
%sythetic = readtable('new.csv');

score = width(sourceTab)*height(sourceTab);
for j = 1:(width(sourceTab))
    for i = 1:(height(sourceTab))
        if not(isequal(sourceTab{i,j},sythetic{i,j}))
             sourceVal = (sourceTab{i,j});
             synthVal = (sythetic{i,j});
             
        else
            score= score - 1;
        end
    end
end

disp((score / (width(sourceTab)*height(sourceTab))*100) + "%")