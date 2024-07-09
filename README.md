# SWS3019-2024

NUS SoC Big Data Analytics and Visualization 2024 Summer Project



## Repository Structure

```
SWS3019-2024
├── code                                     # code for this project
│   ├── Question 1                             # code for question 1 
│   │   ├── Add_belonging_to_house.ipynb         # classify houses' district
│   │   ├── Add_belonging_to_mall.ipynb          # classify malls' district
│   │   ├── BeijingShape.py                      # code to plot Beijing map
│   │   ├── Corr.py                              # calculate correlation matrix
│   │   ├── CorrPlot.py                          # plot correlation matrix
│   │   ├── district_data.py                     # code to get district data
│   │   ├── Fetcher.js                           # script to get mall data
│   │   ├── Judge.py                             # code for judge point in a polygon
│   │   └── MallOperator.js                      # code for get mall location
│   ├── preprocessing.ipynb                    # preprocessing code
│   └── preprocessing_onehot.py                # preprocessing to one-hot code
├── data                                     # data processed and used
│   ├── Beijing_shp                            # geography data of Beijing
│   ├── Beijing_geo.csv                        # geography data of Beijing in csv form
│   ├── BeijingHousingPrices.csv               # origin data
│   ├── BeijingHousingPrices_preprocessed.csv  # data preprocessed
│   ├── BJ1.csv                                # used in one-hot decoding
│   ├── Corr.csv                               # correlation of attribute
│   ├── Corr_mall.csv                          # correlation of attribute with mall_cnt
│   ├── district.csv                           # data about every district
│   ├── house_belonging.csv                    # housing price data with tag belonging
│   ├── Mall.csv                               # data of mall in Beijing
│   ├── mall_belonging.csv                     # mall data with tag belonging
│   └── Subway.csv                             # subway location of Beijing               
├── origin_material                                  
│   ├── BeijingHousingPrices.xlsx              # data used in this project           
│   └── Project.pdf                            # project requirement 
├── pic                                     
│   ├── *.png                                  # data used in this project           
│   └── *.jpg                                  # project requirement
├── .gitignore
├── LICENSE                                  # MIT License
└── README.md
```

