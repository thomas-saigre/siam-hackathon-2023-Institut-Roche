clear
close all

% The raw data
% data = readtable('brca_mRNA_50patients.xls');
data = readtable('brca_mRNA_50patients.csv');
% The dimensions of the table
[ m, N ] = size(data);
data = table2cell(data);

% The result
A = zeros(m,N);

% Populate the result
for i=1:N
    % Work on the current column
    cur = data(:,i);
    
    % Check if it is double
    d = findnumeric(cur);
    
    % If the given data is ALL double, copy-paste it
    if(sum(d)==m)
        A(:,i) = cell2mat(cur);
    else
        d = isequalString(cur, 'Low') | isequalString(cur, 'Moderate') | isequalString(cur, 'High');
        if(sum(d) > 0)
            'Here'
            dd = isequalString(cur,'Low');
            A(dd,i) = 1;
            dd = isequalString(cur,'Moderate');
            A(dd,i) = 2;
            dd = isequalString(cur,'High');
            A(dd,i) = 3;
            A(~d,i) = -100;
        else
            % If there is NA, it means that the rest is numeric
            d = isequalString(cur, 'NA') | isequalString(cur, '');
            if( sum (d) > 0 )
                A(~d,i) = str2double(cur(~d));
                A(d,i) = min(A(:,i)) - 100;
                if(sum(isNaN(A(:,i))) > 0)
                    A(:,i) = label(cur);
                end
            else                
                b = check_binary(cur,m);
                if(b)
                    A(:,i) = assign_binary(cur);
                else
                    
                end
            end
        end
    end
end

function y = check_binary(cur, m)
    label_1 = cur{1};
    label_1_m = isequalString(cur, label_1);
    
    indices = 1:m;
    indices = indices(~label_1_m);
    label_2 = cur{indices(1)};    
    label_2_m = isequalString(cur, label_2);
    
    y = (sum(label_1_m) + sum(label_2_m)) == m;
end

function d = assign_binary(cur)
    d = zeros( length(cur), 1);    
    label_1 = cur{1};
    label_1_m = isequalString(cur, label_1);
    d(label_1_m) = +1;
	d(~label_1_m) = -1;
end

function d = findnumeric(cur)
    d = zeros(size(cur));
    for i=1:length(d)
        d(i) = isnumeric(cur{i});
    end
end

function d = isequalString(cur,label)
    d = false( length(cur), 1);
    for i=1:length(d)        
        d(i) = isequal(cur{i},label);
    end
end
