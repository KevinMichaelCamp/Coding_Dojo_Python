var blobs = [];
        var gravityAcceleration = 0.8;
        function setup(){
            createCanvas(720, 400);
            var x = 1;
            {% for blob in blobs %}
                blobs.push(new Blob("{{blob.team}}", "{{blob.name}}", 60*x, 40*x));
                x++;
            {% endfor %}
        }
        function draw(){
            background('black')
            for(var i = 0;i<blobs.length;i++){
                blobs[i].move();
                blobs[i].display();
            }
        }
        function Blob(team, name, xPosition, yPosition){
            this.team=team;
            this.name=name;
            this.x = xPosition;
            this.y = yPosition;
            this.diameter = 50;
            this.radius = this.diameter/2;
            this.speed = 0;
            this.move = function () {
                this.y += this.speed;
                if (this.y >= (height - this.diameter / 2)) {
                    this.y = height - this.diameter / 2;
                    this.speed = -0.9 * this.speed;
                } else {
                    this.speed += gravityAcceleration;
                }
            }
            this.display = function () {
                fill(this.team);
                ellipse(this.x, this.y, this.diameter, this.diameter);
                fill('white');
                text(this.name, this.x-this.radius ,this.y);
            }
        }
