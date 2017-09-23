library(shiny)
library(leaflet)
library(maps)
interactive()

ui <- fluidPage(
      sidebarPanel(
                   h1('Narrow your search:'), 
                   textInput('state', 'Input state in continental US'),
                   actionButton('statesubmit', 'Submit'),
                   br(),
                   br(),
                   br(),
                   conditionalPanel(
                     condition = "input.statesubmit",
                     color = 'blue',
                     p('Use drop down menu or simply type in desired county'),
                     selectInput(
                       'county', 'List of Counties', c()
                     ),
                     br(),
                     radioButtons('show', 'Highlight county?', choices = c("Yes", "No")),
                     actionButton('countysubmit', 'Submit')
                     
                     
                   )
                   
      ),
      
      mainPanel(
        leafletOutput("CountyMap", width = 1000, height = 500)
      )
)

server <- function(input, output, session){
  observeEvent(input$statesubmit,
        updateSelectInput(session, 'county', choices = map('county', input$state, namesonly = TRUE, plot = FALSE))
  )

  generate_map<-eventReactive(input$countysubmit, {
        if(input$show == "Yes"){
          opac <- 0.1
        }
        else{opac <- 0}

        County <- map('county',input$county, fill = TRUE, plot = FALSE, exact = TRUE)
        
        leaflet(County) %>% addTiles() %>%
          fitBounds(County$range[1], County$range[3], County$range[2], County$range[4])%>%
          addPolygons(fillOpacity = opac, smoothFactor = 0.5, stroke = FALSE, weight = 1)
  })
        output$CountyMap <- renderLeaflet({
          generate_map()
    })

}




shinyApp(ui =ui, server = server)