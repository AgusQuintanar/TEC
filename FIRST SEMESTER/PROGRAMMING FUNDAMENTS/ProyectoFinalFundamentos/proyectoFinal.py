#Proyecto final Fundamentos de Programación  A01636142  A01636166




from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import credenciales
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


#Clase Cliente de TWITTER (Cuenta developer)
class ClienteTwitter():
    def __init__(self, twitter_user=None):
        self.autentificacion = AutentificadorDeTwitter().autoentificar_app_de_twitter()
        self.cliente_twitter = API(self.autentificacion)
        self.twitter_user = twitter_user

    def obtener_API_de_cliente(self):
        return self.cliente_twitter

#Clase de Auntentificacion
class AutentificadorDeTwitter():
    def autoentificar_app_de_twitter(self):
        autentificacion = OAuthHandler(credenciales.CONSUMER_KEY, credenciales.CONSUMER_SECRET)
        autentificacion.set_access_token(credenciales.ACCESS_TOKEN, credenciales.ACCESS_TOKEN_SECRET)
        return autentificacion

# Clase Twitter Streamer, para procesar tweets en vivo.
class TwitterStreamer():
    def __init__(self):
        self.twitter_autenticator = AutentificadorDeTwitter()

    def stream_tweets(self, tweets_recolectados, lista_hash_tag):
        # This handles Twitter autentificacionetification and the connection to Twitter Streaming API
        listener = TwitterListener(tweets_recolectados)
        autentificacion = self.twitter_autenticator.autoentificar_app_de_twitter()
        stream = Stream(autentificacion, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=lista_hash_tag)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, tweets_recolectados):
        self.tweets_recolectados = tweets_recolectados

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweets_recolectados, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


class AnalizadorDeTweet():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def limpiar_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.limpiar_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 'Tweet positivo'
        elif analysis.sentiment.polarity == 0:
            return 'Tweet neutral'
        else:
            return 'Tweet negativo'

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        df['Fecha'] = np.array([tweet.created_at for tweet in tweets])
        df['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['Indice'] = list(range(numero_de_tweets))
        df['Localizacion'] = np.array([tweet.user.location for tweet in tweets])

        return df


if __name__ == '__main__':

    cliente_1 = 'realDonaldTrump'
    cliente_2 = 'yuyacst'
    numero_de_tweets = 10

    cliente_twitter = ClienteTwitter()
    tweet_analyzer = AnalizadorDeTweet()
    api = cliente_twitter.obtener_API_de_cliente()

    tweets_cliente_1 = api.user_timeline(screen_name=cliente_1, count=numero_de_tweets)
    df_cliente_1 = tweet_analyzer.tweets_to_data_frame(tweets_cliente_1)
    df_cliente_1['Polaridad'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df_cliente_1['Tweets']])
    print('Tweets de',cliente_1)
    print(df_cliente_1.head(numero_de_tweets))
    df_cliente_1.to_csv('CSV_de_tweets_cliente_1.csv', encoding='utf-8', index=True)

    tweets_cliente_2 = api.user_timeline(screen_name=cliente_2, count=numero_de_tweets)
    df_cliente_2 = tweet_analyzer.tweets_to_data_frame(tweets_cliente_2)
    df_cliente_2['Polaridad'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df_cliente_2['Tweets']])
    print('\nTweets de', cliente_2)
    print(df_cliente_2.head(numero_de_tweets))
    df_cliente_2.to_csv('CSV_de_tweets_cliente_2.csv', encoding='utf-8', index=True)

    time_likes1 = pd.Series(data=df_cliente_1["Likes"].values, index=df_cliente_1['Indice'])
    time_likes1.plot(figsize=(16, 4), label=f'Likes de {cliente_1}', legend=True)
    time_likes2 = pd.Series(data=df_cliente_2['Likes'].values, index=df_cliente_2['Indice'])
    time_likes2.plot(figsize=(16, 4), label=f'Likes de {cliente_2}', legend=True)
    plt.title('Comparacion de Likes emtre '+cliente_1+' y '+cliente_2)
    plt.show()

    time_retweets1 = pd.Series(data=df_cliente_1['Retweets'].values, index=df_cliente_1['Indice'])
    time_retweets1.plot(figsize=(16, 4), label=f'Retweets de {cliente_1}', legend=True)
    time_retweets2 = pd.Series(data=df_cliente_2['Retweets'].values, index=df_cliente_2['Indice'])
    time_retweets2.plot(figsize=(16, 4), label=f'Retweets de {cliente_2}', legend=True)
    plt.title('Comparacion de Retweets emtre ' + cliente_1 + ' y ' + cliente_2)
    plt.show()



