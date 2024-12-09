COVID Lung X-Rays Classification
==============================


This project is a fork of [MAR24_BDS_Radios_Pulmonaire](https://github.com/DataScientest-Studio/MAR24_BDS_Radios_Pulmonaire) which was made during the Data Scientist course of [Datascientest](https://datascientest.com/) from March to June 2024. It uses the [COVID-QU-Ex dataset](https://www.kaggle.com/datasets/anasmohammedtahir/covidqu) available on Kaggle.

View the original streamlit app on [Huggingface](https://huggingface.co/spaces/fdayde/streamlit-dl-radio)

------------
### References

[1] A. M. Tahir, M. E. H. Chowdhury, A. Khandakar, Y. Qiblawey, U. Khurshid, S. Kiranyaz, N. Ibtehaz, M. S. Rahman, S. Al-Madeed, S. Mahmud, M. Ezeddin, K. Hameed, and T. Hamid, “COVID-19 Infection Localization and Severity Grading from Chest X-ray Images”, Computers in Biology and Medicine, vol. 139, p. 105002, 2021, https://doi.org/10.1016/j.compbiomed.2021.105002.  
[2] Anas M. Tahir, Muhammad E. H. Chowdhury, Yazan Qiblawey, Amith Khandakar, Tawsifur Rahman, Serkan Kiranyaz, Uzair Khurshid, Nabil Ibtehaz, Sakib Mahmud, and Maymouna Ezeddin, “COVID-QU-Ex .” Kaggle, 2021, https://doi.org/10.34740/kaggle/dsv/3122958.  
[3] T. Rahman, A. Khandakar, Y. Qiblawey A. Tahir S. Kiranyaz, S. Abul Kashem, M. Islam, S. Al Maadeed, S. Zughaier, M. Khan, M. Chowdhury, "Exploring the Effect of Image Enhancement Techniques on COVID-19 Detection using Chest X-rays Images," Computers in Biology and Medicine, p. 104319, 2021, https://doi.org/10.1016/j.compbiomed.2021.104319.  
[4] A. Degerli, M. Ahishali, M. Yamac, S. Kiranyaz, M. E. H. Chowdhury, K. Hameed, T. Hamid, R. Mazhar, and M. Gabbouj, "Covid-19 infection map generation and detection from chest X-ray images," Health Inf Sci Syst 9, 15 (2021), https://doi.org/10.1007/s13755-021-00146-8.  
[5] M. E. H. Chowdhury, T. Rahman, A. Khandakar, R. Mazhar, M. A. Kadir, Z. B. Mahbub, K. R. Islam, M. S. Khan, A. Iqbal, N. A. Emadi, M. B. I. Reaz, M. T. Islam, "Can AI Help in Screening Viral and COVID-19 Pneumonia?," IEEE Access, vol. 8, pp. 132665-132676, 2020, https://doi.org/10.1109/ACCESS.2020.3010287.

------------
### Original project team: 
- Thomas Baret [linkedin](https://linkedin.com/in/thomas-baret-080050107) [github](https://github.com/tom-b974)
- Nicolas Bouzinbi [linkedin](https://linkedin.com/in/nicolas-bouzinbi-7916481b4) [github](https://github.com/NicolasBouzinbi)
- Florent Daydé [linkedin](https://linkedin.com/in/florent-daydé-16431469) [github](https://github.com/fdayde)
- Nicolas Fenassile [linkedin](https://linkedin.com/in/nicolasfenassile) [github](https://github.com/NicoFena)

supervised by: Gaël Penessot

------------
How to deploy the streamlit app on Huggingface: 

- Create a new space on Huggingface and clone the repository
- Push the content of the `src/streamlit` directory
- Add the model's weights file to the `models` folder
- Store the model weights in Git LFS by adding the following line to the `.gitattributes` file:  
```*.h5 filter=lfs diff=lfs merge=lfs -text```
- Push to Huggingface
- Do not modify or delete the `REAMDE.md` file created by Huggingface during the initialization on the space.

------------
Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── demo               <- Samples from the dataset for demonstration in streamlit
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries, not on Github for size reasons
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    │
    ├── reports            <- The final report made during this project (PDF)
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │   
    │   │── streamlit      <- Scripts for the Streamlit app
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
