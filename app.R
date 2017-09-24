library(shiny)
library(leaflet)
library(maps)

ui <- fluidPage(
      sidebarPanel(
                   h1('Narrow your search:'), 
                   textInput('state', 'Input state in continental US'),
      tags$head(tags$style(
        HTML('
             #outerpan {background-color: rgba(255,255,255,0.8); padding:1%}
             ')
              
        )),
  
      leafletOutput("CountyMap", width = '100%', height = 750),
      absolutePanel(id ='outerpan', width = '20%', top = '5%', right = '3%', draggable = TRUE,
                  
                   h1('Narrow your search:'), 
                   textInput('state', 'Input state in continental US', placeholder = 'texas'),
                   actionButton('statesubmit', 'Submit'),
                   br(),
                   br(),
                   br(),
                   conditionalPanel(
                     condition = "input.statesubmit",
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
                     actionButton('countysubmit', 'Submit'),
                     br(),
                     p('Click and drag panel to move it')
                     
                   )
                   
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
        County <- map('county',input$county, fill = TRUE, plot = FALSE, exact = TRUE)

        leaflet(County) %>% addTiles() %>%
          fitBounds(County$range[1], County$range[3], County$range[2], County$range[4])%>%
          addPolygons(fillOpacity = opac, fillColor = "#000", smoothFactor = 0.5, stroke = FALSE)%>%
          addCircleMarkers(mean(County$x),mean(County$y), radius = 5, fillColor = "#F00", color = "F00", fillOpacity = 1,
                           popup = paste0(round(County$x,4),',',round(County$y,4)), popupOptions = list(closeOnClick = TRUE, 
                                                                                                        closeButton = FALSE))
  })
        output$CountyMap <- renderLeaflet({
          generate_map()
    })

}




shinyApp(ui =ui, server = server)