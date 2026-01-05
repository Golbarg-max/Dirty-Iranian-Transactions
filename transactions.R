# Transaction Data Analysis in R
# Author: Golbarg Ghazinour
# Date: December 2025

#Load libraries
library(tidyverse)

#Load data
transactions <- read_csv("transactions_clean.csv")

#Explore data
glimpse(transactions)
summary(transactions)

# Analysis 1: Overall success rate
transactions %>%
  summarise(
    total_transactions = n(),
    successful = sum(status =="success"),
    success_rate = (successful / total_transactions) * 100
  )

# Analysis 2: Success rate by card type
transactions %>%
  filter(!is.na(card_type)) %>%
  group_by(card_type) %>%
  summarise(
    total_transactions = n(),
    successful = sum(status =="success"),
    success_rate = (successful / total_transactions) * 100
  ) %>%
  ggplot(aes(x = reorder(card_type, success_rate), y = success_rate)) + 
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "Success Rate by Card Type",
    x = "Card Type",
    y = "Success Rate (%)"
  ) + 
  theme_minimal()
  
transactions %>%
  count(status) %>%
  ggplot(aes(x = "", y = n, fill = status)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y") +
  scale_fill_manual(values = c("fail" = "#FF6B6B", "success" = "#4ECDC4")) +
  labs(title = "Transaction State Distribution") +
  theme_void()

transactions %>% 
  mutate(date = as.Date(time)) %>%
  count(date) %>%
  ggplot(aes(x = date, y = n)) +
  geom_line(color = "steelblue", size = 1) + 
  labs (
    title = "Daily Transaction Volume",
    x = "Date",
    y = "Number of Transactions"
  ) +
  theme_minimal()
  
transactions %>%
  filter(!is.na(city)) %>%
  count(city, sort = TRUE) %>%
  top_n(5) %>%
  ggplot(aes(x = reorder(city, n), y = n)) +
  geom_col(fill = "coral") +
  coord_flip() +
  labs (
    title = "Top 5 Cities by Transaction Volume",
    x = "City",
    y = "Number of Transactions"
  ) +
  theme_minimal()

