$(document).ready(function(){
    
    // Add To Selection
    $(".add-to-selection").on("click", function(){

        let button = $(this)
        let id = button.attr("data-index")

        let hotel_id = $("#id").val()
        let room_id = $(`.room_id_${id}`).val()
        let room_number = $(`.room_number_${id}`).val()
        let hotel_name = $("#hotel_name").val()
        let room_name = $("#room_name").val()
        let room_price = $("#room_price").val()
        let number_of_beds = $("#number_of_beds").val()
        let room_type = $("#room_type").val()
        let checkin = $("#checkin").val()
        let checkout = $("#checkout").val()
        let adult = $("#adult").val()
        let children = $("#children").val()

        console.log(`${id} Added To Selection`);
        console.log(`hotel_id: ${hotel_id}`);
        console.log(`room_number: ${room_number}`);
        console.log(`room_id: ${room_id}`);
        console.log(`hotel_name: ${hotel_name}`);
        console.log(`room_name: ${room_name}`);
        console.log(`room_price: ${room_price}`);
        console.log(`number_of_beds: ${number_of_beds}`);
        console.log(`room_type: ${room_type}`);
        console.log(`checkin: ${checkin}`);
        console.log(`checkout: ${checkout}`);
        console.log(`adult: ${adult}`);
        console.log(`children: ${children}`);


        $.ajax({
            url:'/booking/add_to_selection/',
            data: {
                'id': id,
                'hotel_id': hotel_id,
                'hotel_name': hotel_name,
                'room_number': room_number,
                'room_name': room_name,
                'room_price': room_price,
                'number_of_beds': number_of_beds,
                'room_type': room_type,
                'room_id': room_id,
                'checkin': checkin,
                'checkout': checkout,
                'adult': adult,
                'children': children,
            },
            dataType: 'json',
            beforeSend: function(){
                console.log("Adding room...");
                button.html("<i class='fas fa-clock-rotate-left'></i> Adding room... ")
            },
            success: function(response){
                button.html("<i class='fas fa-check-circle'></i> Added to selection ")

                console.log("Added Room To Selection!");
                $(".room-count").text(response.total_selected_items)
                
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 1000,
                    timerProgressBar: true,
                })
                    
                Toast.fire({
                    icon: 'success',
                    title: 'Added Room To Selection!'
                })
            }
        })

    })
})

$(document).on('click','.delete-item',function(){
    var id = $(this).attr('data-item');
    var button = $(this);
    
    $.ajax({
        url:'/booking/delete_selection/',
        data:{
            'id':id,
        },
        dataType:'json',
        beforeSend:function(){
            button.text('...');
        },
        success:function(res){
            $(".room-count").text(res.total_selected_items);
            $(".selection-list").html(res.data);

            if (res.total_selected_items < 1) {
                Swal.fire({
                    icon: 'warning',
                    title: 'No Selections Yet...',
                    text: "Add some selection to continue to cart..."
                }).then((result) => {
                    window.location.href = "/"
                  });

                
            }
        }
    });
}); 