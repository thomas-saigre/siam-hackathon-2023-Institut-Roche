clear
close all

% The raw data

data_1 = readtable('brca_mRNA_1977patients.csv');
data_2 = readtable('PrivBayes\brca_mRNA_patients_PrivBayes_n20_deg2_eps1_seed_8.csv');
[ m_original, N_original ] = size(data_1);

data_1 = table2cell(data_1);
data_2 = table2cell(data_2);

for i=[4,6,7,9,10]
    for j=1:m_original
        data_2{j,i} = num2str(data_2{j,i});
    end
end

data = vertcat(data_1, data_2);

% The dimensions of the table
[ m, N ] = size(data);

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
                if(sum(isnan(A(:,i))) > 0)
                    A(:,i) = assign_labels(cur);
                end
            else                
                b = check_binary(cur,m);
                if(b)
                    A(:,i) = assign_binary(cur);
                else
                    A(:,i) = assign_labels(cur);
                end
            end
        end
    end
end

I = isnan(A);
A(I) = -100;

A_1 = A(m_original+1:end, :);
save brca_mRNA_patients_PrivBayes_n20_deg2_eps1_seed_8 A_1

A = A(1:m_original, :);
save brca_mRNA_50patients A

%%% HELPER FUNCTIONS
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

function a = assign_labels(cur)    
    m = length(cur);
    a = zeros( m, 1);
    i = 1;
    assigned = a;
    indices = 1:m;
    
    while(sum(assigned) < m)
        label = cur{indices(1)};
        label_m = isequalString(cur, label);
        a(label_m) = i;
        
        i = i + 1;
        
        assigned = assigned | label_m;
        indices = 1:m;
        indices = indices(~assigned);
    end
end