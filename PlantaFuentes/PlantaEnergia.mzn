% Parameters
int: n; % Number of days in the planning horizon
int: m; % Number of customers
int: consecutive_high_days_allowed; % Number of consecutive days allowed in high regime
int: high_regime_percentage; % Percentage of capacity considered high regime
set of int: DAYS = 1..n;
set of int: CUSTOMERS = 1..m; 
set of int: PLANTS = 1..3; % Set of energy plants: 1-Nuclear, 2-Hydroelectric, 3-Thermal

array[DAYS] of var 0..n: days_in_high_regime;
array[PLANTS] of int: capacity; % Daily production capacity for each plant
array[PLANTS] of float: production_cost; % Production cost per MW for each plant
array[CUSTOMERS,DAYS] of int: demand; % Daily demand for each customer
array[CUSTOMERS] of float: payment_per_mw; % Payment per MW for each customer 
int: G; % Minimum percentage of demand that must be satisfied

% Variables
array[PLANTS,DAYS] of var int: production; % Daily production for each plant
array[CUSTOMERS,DAYS] of var int: delivered; % Energy delivered to each customer

% Constraints

% Total daily production must not exceed plant capacity
constraint forall(d in DAYS, p in PLANTS) (
    production[p,d] <= capacity[p] /\ production[p,d] >= 0
);

% Energy delivered to each customer must be equal to their demand or at least G% of the demand if full satisfaction is not possible
constraint forall(c in CUSTOMERS, d in DAYS) (
    delivered[c,d] >= (G/100) * demand[c,d] /\ delivered[c,d] <= demand[c,d]
);

% Total delivered energy must not exceed total production
constraint forall(d in DAYS) (
    sum(c in CUSTOMERS) (delivered[c,d]) <= sum(p in PLANTS) (production[p,d])
);


% High regime constraints for the Hydroelectric plant

constraint days_in_high_regime[1] = if production[2,1] > (high_regime_percentage/100) * capacity[2] then 1 else 0 endif;

constraint forall(d in 2..n) (
    days_in_high_regime[d] = 
    if production[2,d] > (high_regime_percentage/100) * capacity[2] then
        days_in_high_regime[d-1] + 1
    else
        0
    endif
);

constraint forall(d in DAYS) (
    days_in_high_regime[d] <= consecutive_high_days_allowed
);


% Objective: Maximize net profit
var float: net_profit = sum(c in CUSTOMERS, d in DAYS) (delivered[c,d] * payment_per_mw[c]) - 
                        sum(p in PLANTS, d in DAYS) (production[p,d] * production_cost[p]);
                    
solve maximize net_profit;

% Show the solutions
output [ 
    "Net Profit: ", show(net_profit), "\n",
    "Production:\n"
] ++
[ 
    if d == 1 then
        "Plant " ++ show(p) ++ ": " ++ show(production[p,d])
    else
        ", " ++ show(production[p,d])
    endif ++
    if d == n then
        "\n"
    else
        ""
    endif
    | p in PLANTS, d in DAYS
] ++
[ 
    "Delivered:\n"
] ++
[ 
    if d == 1 then
        "Customer " ++ show(c) ++ ": " ++ show(delivered[c,d])
    else
        ", " ++ show(delivered[c,d])
    endif ++
    if d == n then
        "\n"
    else
        ""
    endif
    | c in CUSTOMERS, d in DAYS
];



