%% Practice using SHEBA data to find eps_sky and Calibrate Brunt Eq.
% Jason Kniss 2/1/24
% Data from 20180506

% The data used for these plots and calculations come from the SHEBA 
% dataset "Tower, Interpolated hourly measurements to 2.5 and 10m at Met
% City (ASFG) [Andreas, E., C. Fairall, P. Guest, O. Persson]" 

% The data includes readings from instruments set on a tower at 2.5m and
% 10m heights. Correlated measurements/calcs will be identifiable in the code 
% by the suffixes '2' and '10' respectively.
%% Clean
clc; clear; close all;

%% Read in data 
% ...As table (not sure why I couldn't do it as a matrix)
tower_2_raw = readtable('main_file6_hd');

%% Convert table data to matrix
% % This coice has more to do with skill level than efficiency
tower_2_mat = table2array(tower_2_raw);

% Change flagged measurements to NaN (flagged as 9999 or 999)
tower_2_mat(tower_2_mat == 9999) = NaN;
tower_2_mat(tower_2_mat == 999) = NaN;

% Create vectors (I'll have an easier time converting things this way) 
jd = tower_2_mat(:,1); % time (Julian Day)
Pa = tower_2_mat(:,4); % air pressure (mb)
T2 = tower_2_mat(:,9); % 2.5m temperature reading (C)
T10 = tower_2_mat(:,10); % 10m temperature reading (C)
q2 = tower_2_mat(:,11); % 2.5m water vapor content (g/kg_air)
q10 = tower_2_mat(:,12); % 10m water vapor content (g/kg_air)
DLR = tower_2_mat(:,19); % Downwelling Longwave DLR (W/m^2)

%% Convert Julian Day to MATLAB datetime
jd = jd + 2450449.5;
t = datetime(jd, 'ConvertFrom', 'juliandate', ...
    'Format', 'dd-MMM-yyyy HH:mm:ss');
%%
% Convert units to match equation from (1)
Pa = Pa * 100; % Convert air pressure from mb to Pa
T2 = T2 + 273.15; % Convert Temperature from C to K
T10 = T10 + 273.15; % Convert Temperature from C to K
q2 = q2/1000; % Convert water content from g/kg to kg/kg
q10 = q10/1000; % Convert water content from g/kg to kg/kg

% Define Constants
sigma = 5.68E-8; % Stefan-Boltzman constant

% Calculate emissivity
eps_cs2 = DLR ./ (sigma * T2.^4);
eps_cs10 = DLR ./ (sigma * T10.^4);

%% Brunt Model Calculation
% Convert water vapor content to partial pressure of water vapor (hPa)
Pw2 = ((q2 .* Pa)./(q2 + .622))/100; 
Pw10 = ((q10 .* Pa)./(q10 + .622))/100;

% Calculate expected DLR based on original Brunt Model (2)
eps_b2 = 0.52 + 0.065*sqrt(Pw2);
eps_b10 = 0.52 + 0.065*sqrt(Pw10); % clear sky emissivity from Brunt eq

% % Calculate expected DLR based on calibrated Brunt Model (1)
% eps_b2 = 0.618 + 0.054*sqrt(Pw2);
% eps_b10 = 0.618 + 0.054*sqrt(Pw10); % clear sky emissivity

DLR_exp2 = eps_b2*sigma.*T2.^4;
DLR_exp10 = eps_b10*sigma.*T10.^4; % Expected DLR based on Brunt eq

%% Generate plots
figure(1)
grid on; hold on;
validIndices = ~isnan(eps_cs2);
scatter(t(validIndices),eps_cs2(validIndices), .5, 'b');
validIndices = ~isnan(eps_cs10);
scatter(t(validIndices),eps_cs10(validIndices), .5, 'r');
title('Calculated Emissivity over Time')
legend('2.5m readings','10m readings')
% Customize the x-axis labels
xticks(t(1:1000:end));  % Display every 50th date
xtickformat('dd-MMM-yyyy HH:mm:ss');
xlabel('Date and Time');
ylabel('emissivity');

% Expected vs Measured DLR based on 2.5m measurements
figure(2)
grid on; hold on;
validIndices = ~isnan(DLR) & ~isnan(DLR_exp2);
scatter(DLR(validIndices),DLR_exp2(validIndices), .5, 'b');

% Insert a black line to mark expected = measured
line([0, max(max(DLR(validIndices)),max(DLR_exp2(validIndices)))], ...
    [0, max(max(DLR(validIndices)),max(DLR_exp2(validIndices)))], ...
    'Color', 'k', 'LineStyle', '-');

% Customize the x-axis labels
% xticks(t(1:1000:end));  % Display every 50th date
% xtickformat('dd-MMM-yyyy HH:mm:ss');
title('measured vs expected DLR')
xlabel('Measured DLR');
ylabel('Expected DLR');
axis([0, max(max(DLR(validIndices)),max(DLR_exp2(validIndices))), 0, ...
    max(max(DLR(validIndices)),max(DLR_exp2(validIndices)))])

% Expected vs Measured DLR based on 10m measurements
figure(3)
grid on; hold on;
validIndices = ~isnan(DLR) & ~isnan(DLR_exp10);
scatter(DLR(validIndices),DLR_exp10(validIndices), .5, 'r')

% Insert a black line to mark expected trendline
line([0, max(max(DLR(validIndices)),max(DLR_exp10(validIndices)))], ...
    [0, max(max(DLR(validIndices)),max(DLR_exp10(validIndices)))], ...
    'Color', 'k', 'LineStyle', '-');

% Customize the x-axis labels
% xticks(t(1:1000:end));  % Display every 50th date
% xtickformat('dd-MMM-yyyy HH:mm:ss');
title('measured vs expected DLR')
xlabel('Measured DLR');
ylabel('Expected DLR');
axis([0, max(max(DLR(validIndices)),max(DLR_exp10(validIndices))), 0, ...
    max(max(DLR(validIndices)),max(DLR_exp10(validIndices)))])




%% References
% (1) M. Li, Y. Jiang, and C. F. M. Coimbra (2017) “On the Determination of
%     Atmospheric Longwave Irradiance Under All-Sky Conditions," Solar Energy 
%     (144), pp. 40–48. 
% (2) Brunt, D., 1932. Notes on radiation in the atmosphere. I. Quart. J. 
%     Roy. Meteorol. Soc. 58 (247), 389–420.
