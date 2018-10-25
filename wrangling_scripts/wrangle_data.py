import pandas as pd
from functools import reduce
import plotly
import plotly.graph_objs as go
import scipy
import plotly.figure_factory as ff
import pycountry

  

def cleandata(dataset, year=2017):


  """Clean world happiness data for a visualizaiton dashboard

  Keeps data range of dates in keep_columns variable and drop columns
  that were not common between 2015 to 2017
  return columns with a corresponding name as suffix


  Args:
      dataset (str): name of the csv data file

  Returns:
      dataframe with clean columns
  """    
  keepcolumns_list= ['Country', 'Happiness (Rank)', 'Happiness (Score)', 'Economy (GDP.per.Capita)', 'Family','Health (Life.Expectancy)', 'Freedom', 'Generosity','Trust (Government.Corruption)', 'Dystopia (Residual)']
  df = pd.read_csv(dataset)
  if (year == 2017):
      dropcolumns = ['Whisker.high', 'Whisker.low']

  if (year == 2016):
      dropcolumns = ['Region', 'Lower Confidence Interval', 'Upper Confidence Interval']

  if (year ==2015):
      dropcolumns = ['Region', 'Standard Error']

  df.drop(columns = dropcolumns, inplace = True)

  df.columns = [col+'_'+str(year)  if col != 'Country' else col for col in keepcolumns_list]


  return df




def basic_wrangling():

    """joins happiness data for a visualizaiton dashboard for 2015 to 2017
    and return the joint dataframe


    Args:
        None

    Returns:
        dataframe 
    """  

    df_2017 = cleandata("data/2017.csv", year = 2017)
    df_2016 = cleandata("data/2016.csv", year = 2016)
    df_2015 = cleandata("data/2015.csv", year = 2015)
    dfs = [df_2017, df_2016, df_2015]
    df_final = reduce(lambda left,right: pd.merge(left,right,on='Country'), dfs)


    input_countries = df_final['Country']
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

 

    df_final['Country_code'] = df_final['Country'].apply(lambda x: countries.get(x, 'Unknown code'))
    #print(df_final.head())
    #print(df_final[df_final['Country_code']!='Unknown code'])

    return df_final



def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    df_final = basic_wrangling()

    color_scale = [[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'],\
     [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],\
     [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']]

    #  Graph one

    x_val = df_final['Happiness (Rank)_2017']
    y_val = df_final['Happiness (Rank)_2016']
    country = df_final['Country']
    color_ = df_final['Trust (Government.Corruption)_2017']

    graph_one = []
    graph_one.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    opacity= 0.3    
                   ),
        text = country,
        name = '2017 vs. 2016'
        ))

    layout_one = dict(title = 'Happiness Rank correlation 2016/2015 vs. 2017',
        xaxis = dict(title = 'Happiness Rank 2017'),
        yaxis = dict(title = 'Happiness Rank 2016/2015'),
        )



    # Graph two add to one

    x_val = df_final['Happiness (Rank)_2017']
    y_val = df_final['Happiness (Rank)_2015']
    country = df_final['Country']
    


    graph_one.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    opacity= 0.3    
                   ),
        text = country,
        name = '2017 vs. 2015'
        ))




    # Graph three


    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Economy (GDP.per.Capita)_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_three = []
    graph_three.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3 ,  showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country
        ))

    layout_three = dict(title = 'Happiness Score correlation with Economy (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
        yaxis = dict(title = 'Economy (GDP per Capita) 2017'),
        )


    #Graph four
    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Family_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_four = []
    graph_four.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3,showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country
        ))

    layout_four = dict(title = 'Happiness Score correlation with Family (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
        yaxis = dict(title = 'Family 2017'),
        )


    #Graph five
    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Health (Life.Expectancy)_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_five = []
    graph_five.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3,showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country
        #name = country
        ))

    layout_five = dict(title = 'Happiness Score correlation with Health (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
        yaxis = dict(title = 'Health (Life Expectancy) 2017'),
        )

    #Graph six
    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Freedom_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_six = []
    graph_six.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3,showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country
        ))

    layout_six = dict(title = 'Happiness Score correlation with Freedom (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
         yaxis = dict(title = 'Freedom 2017'),
        )   

    #Graph seven  
    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Generosity_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_seven = []
    graph_seven.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3,showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country
        ))

    layout_seven = dict(title = 'Happiness Score correlation with Generosity (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
        yaxis = dict(title = 'Generosity 2017'),
        )  


    #Graph eight
    x_val = df_final['Happiness (Score)_2017']
    y_val = df_final['Trust (Government.Corruption)_2017']
    country = df_final['Country']
    color_ = df_final['Happiness (Rank)_2017']

    graph_eight = []
    graph_eight.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= color_,
                    opacity= 0.3,showscale=True,colorscale = color_scale,reversescale = True
                   ),
        text = country

        ))

    layout_eight = dict(title = 'Happiness Score correlation with goverment corruption (2017)',hovermode= 'closest',
        xaxis = dict(title = 'Happiness Score 2017'),
          #autotick=False, tick0=1990, dtick=25),
        yaxis = dict(title = 'Trust (goverment corruption) 2017'),
        )  


    # Graph nine

    chart1 = go.Histogram(
    x=df_final['Happiness (Score)_2017'],name='Happiness (Score)_2017',
    opacity=0.3)

    chart2 = go.Histogram(
    x=df_final['Happiness (Score)_2016'],name='Happiness (Score)_2016',
    opacity=0.3)

    chart3 = go.Histogram(
    x=df_final['Happiness (Score)_2015'],name='Happiness (Score)_2015',
    opacity=0.3)    


    graph_nine = [chart1,chart2,chart3]
    group_labels = ['Happiness (Score)_2017', 'Happiness (Score)_2016', 'Happiness (Score)_2015']

    layout_nine = go.Layout(
    title='Happiness Score distribution 2015-2017',
    xaxis=dict(
        title='Happiness Score'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.1,
    bargroupgap=0.5,
    barmode='overlay'
    )




    # graph 10
    graph_ten = []
    graph_ten = [dict(
            type = 'choropleth',
            locations = df_final['Country'],
            locationmode = 'country names',
            z = df_final['Happiness (Score)_2017'],
            text = df_final['Country'],
            colorscale = [[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'],\
             [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],\
              [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']],
            autocolorscale = False,
            reversescale = False,
            colorbar = dict(
                autotick = False,
                title = 'Happiness Score 2017'),
          )]

    layout_ten = dict(title = '2017 Global Happiness Score',hovermode= 'closest',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    graph_eleven = []
    graph_eleven = [dict(
            type = 'choropleth',
            locations = df_final['Country'],
            locationmode = 'country names',
            z = df_final['Trust (Government.Corruption)_2017'],
            text = df_final['Country'],
            colorscale = [[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'],\
             [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],\
              [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']],
            autocolorscale = False,
            reversescale = False,
            colorbar = dict(
                autotick = False,
                title = 'Trust (Government Corruption) 2017'),
          )]

    layout_eleven= dict(title = 'Trust (Government Corruption) 2017',hovermode= 'closest',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )


    graph_twelve = []
    graph_twelve = [dict(
            type = 'choropleth',
            locations = df_final['Country'],
            locationmode = 'country names',
            z = df_final['Freedom_2017'],
            text = df_final['Country'],
            colorscale = [[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'],\
             [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],\
              [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']],
            autocolorscale = False,
            reversescale = False,
            colorbar = dict(
                autotick = False,
                title = 'Freedom 2017'),
          )]

    layout_twelve= dict(title = 'Freedom 2017',hovermode= 'closest',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )    

    graph_thirteen = []
    df_top = df_final[df_final['Happiness (Rank)_2017']<11]
    df_bottom = df_final[df_final['Happiness (Rank)_2017']>(df_final['Happiness (Rank)_2017'].max()-11)]

    df_top.sort_values('Happiness (Rank)_2017', ascending = True, inplace=True)
    df_bottom.sort_values('Happiness (Rank)_2017', ascending = True, inplace=True)

    graph_thirteen.append(
      go.Bar(
      x = df_top['Country'],
      y = df_top['Happiness (Rank)_2017'],opacity=0.6,
      )
    )

    layout_thirteen = dict(title = 'Top 10 Country Ranked in Happiness 2017 ',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Happiness (Rank) 2017',
        autotick=False,
        ticks='outside',range=[0,10]),
                )    

    graph_fourtheen = []


    graph_fourtheen.append(
      go.Bar(
      x = df_bottom['Country'],
      y = df_bottom['Happiness (Rank)_2017'],marker=dict(
        color='rgba(222,45,38,0.8)'),opacity=0.6,
      )
    )

    layout_fourtheen = dict(title = 'Bottom 10 Country Ranked in Happiness 2017 ',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Happiness (Rank) 2017',
        autotick=False,
        ticks='outside',range=[143,154]),
                )  



#     df.sort_values('Rural_population', ascending=False, inplace=True)
#     df = df[df['year'] == 2015] 

#     graph_five.append(
#       go.Bar(
#       x = df.country.tolist(),
#       y = df.Rural_population.tolist(),
#       )
#     )

#     layout_five = dict(title = 'Rural population in 2015',
#                 xaxis = dict(title = 'Country',),
#                 yaxis = dict(title = 'Rural population'),
#                 )


    
    # append all charts to the figures list
    figures = []

    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))
    figures.append(dict(data=graph_seven, layout=layout_seven))
    figures.append(dict(data=graph_eight, layout=layout_eight))    
    figures.append(dict(data=graph_nine, layout=layout_nine)) 
    figures.append(dict(data=graph_ten, layout=layout_ten)) 
    figures.append(dict(data=graph_eleven, layout=layout_eleven))
    figures.append(dict(data=graph_twelve, layout=layout_twelve))
    figures.append(dict(data=graph_thirteen, layout=layout_thirteen))  
    figures.append(dict(data=graph_fourtheen, layout=layout_fourtheen))    
    return figures