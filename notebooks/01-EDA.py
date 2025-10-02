#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Configurações
%matplotlib inline
sns.set_style('whitegrid')

#%%
# Carregar dados de orders / loanding orders dataset
df_orders = pd.read_csv('../data/raw/olist_orders_dataset.csv')
df_orders.head()

#%%
# Informações gerais
df_orders.info()

#%%
# Estatísticas básicas
df_orders.describe()

#%%
# Contagem de status dos pedidos
df_orders['order_status'].value_counts()

##-------------------------------------------------------------------------------

# %%
#Carregar dados de reviews / loanding reviews dataset
df_reviews = pd.read_csv('../data/raw/olist_order_reviews_dataset.csv')

#%%
# Informações gerais
df_orders.info()

#%%
# Estatísticas básicas
df_orders.describe()

#%%
# Contagem de status dos pedidos
df_orders['order_status'].value_counts()


##-------------------------------------------------------------------------------

# %%
#Carregar dados de pagamentos / loanding payments dataset
df_pay = pd.read_csv('../data/raw/olist_order_payments_dataset.csv')

#%%
df_pay.head()
#%%
# Informações gerais
df_pay.info()

#%%
# Estatísticas básicas
df_pay.describe()

#%%
# Contagem de status dos pedidos
df_pay['order_id'].value_counts()


##-------------------------------------------------------------------------------
#Carregar dados de pagamentos / loanding payments dataset
df_customers = pd.read_csv('../data/raw/olist_customers_dataset.csv')

df_customers.head()

df_customers.info()

df_customers.describe()

#%%
##-------------------------------------------------------------------------------
#Carregar dados de pagamentos / loanding payments dataset
df_products = pd.read_csv('../data/raw/olist_products_dataset.csv')

df_products.head()

#%%
# Informações gerais
df_products.info()

#%%
# Estatísticas básicas
df_products.describe()


#%%
# Contagem de category_name dos product
df_products['product_category_name'].value_counts()


#%%

df_clientes     = pd.read_csv('../data/raw/olist_customers_dataset.csv')
df_geolocacao    = pd.read_csv('../data/raw/olist_geolocation_dataset.csv')
df_order_itens   = pd.read_csv('../data/raw/olist_order_items_dataset.csv')
df_order_pg      = pd.read_csv('../data/raw/olist_order_payments_dataset.csv')
df_order_reviews = pd.read_csv('../data/raw/olist_order_reviews_dataset.csv')
df_ordens        = pd.read_csv('../data/raw/olist_orders_dataset.csv')
df_produtos      = pd.read_csv('../data/raw/olist_products_dataset.csv')
df_vendedores    = pd.read_csv('../data/raw/olist_sellers_dataset.csv')


#%%


##--------------------------------------
## Criacao de inventario dos datasets
##--------------------------------------

def create_data_inventory(df, output_path='data_inventory.csv', save_csv=True):
    """
    Cria um inventário de dados para qualquer DataFrame.
    
    Parâmetros:
    - df: pandas.DataFrame
    - output_path: str, caminho do CSV para salvar (padrão: 'data_inventory.csv')
    - save_csv: bool, se True salva o CSV, se False apenas retorna o DataFrame
    
    Retorna:
    - pd.DataFrame com inventário
    """
    
    # Identificar colunas numéricas e categóricas
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # Criar o inventário
    inventory = pd.DataFrame({
        'coluna': df.columns,
        'tipo': df.dtypes.astype(str),
        'nulos': df.isnull().sum(),
        'percentual_nulos': round(df.isnull().sum() / len(df) * 100, 2),
        'unique': df.nunique(),
        'tipo_variavel': ['Numérica' if col in numeric_cols else 'Categórica' for col in df.columns]
    })

    # Adicionar percentual de nulos (opcional, útil)
    inventory['percentual_nulos'] = round(inventory['nulos'] / len(df) * 100, 2)
    
    # Salvar CSV se solicitado
    if save_csv:
        # Garantir que o diretório existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        inventory.to_csv(output_path, index=False)
        print(f"Inventário salvo em: {output_path}")
    
    return inventory


#%%
'''
df_clientes     = pd.read_csv('../data/raw/olist_customers_dataset.csv')
df_geolocacao    = pd.read_csv('../data/raw/olist_geolocation_dataset.csv')
df_order_itens   = pd.read_csv('../data/raw/olist_order_items_dataset.csv')
df_order_pg      = pd.read_csv('../data/raw/olist_order_payments_dataset.csv')
df_order_reviews = pd.read_csv('../data/raw/olist_order_reviews_dataset.csv')
df_ordens        = pd.read_csv('../data/raw/olist_orders_dataset.csv')
df_produtos      = pd.read_csv('../data/raw/olist_products_dataset.csv')
df_vendedores    = pd.read_csv('../data/raw/olist_sellers_dataset.csv')
'''

create_data_inventory(df_clientes, '../data/inventories/clientes_inventory.csv')
create_data_inventory(df_geolocacao, '../data/inventories/geolocation_inventory.csv')
create_data_inventory(df_order_itens, '../data/inventories/order_items_inventory.csv')
create_data_inventory(df_order_pg, '../data/inventories/payments_inventory.csv')
create_data_inventory(df_order_reviews, '../data/inventories/reviews_inventory.csv')
create_data_inventory(df_ordens, '../data/inventories/orders_inventory.csv')
create_data_inventory(df_produtos, '../data/inventories/products_inventory.csv')
create_data_inventory(df_vendedores, '../data/inventories/sellers_inventory.csv')


