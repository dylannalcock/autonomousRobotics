# Project 4: Planning [![tests](../../../badges/submit-proj4/pipeline.svg)](../../../pipelines/submit-proj4/latest)

Replace this with your own writeup! Please place all figures in this directory.


1. ![](./map2_shortest_path.png)

2. CR: 100 --> Path Length: 362.886,  Plan Time: 1.643824 \
   CR: 80  --> Path Length: 362.907,  Plan Time: 1.012381 \
   CR: 75  --> Path Length: 362.973,  Plan Time: 0.899683 \
   CR: 70  --> Path Length: 362.973,  Plan Time: 0.793863 \
   CR: 65  --> Path Length: 363.068,  Plan Time: 0.700638 \
   CR: 60  --> NO PATH\

3. VN: 600 --> Path Length: 362.88692665140957, Plan Time: 1.6686322689056396 \
   VN: 575 --> Path length: 362.88692665140957, Plan Time: 1.4809751510620117 \
   VN: 550 --> Path length: 362.88692665140957, Plan Time: 1.2958452701568604 \
   VN: 545 --> Path length: 362.88692665140957, Plan Time: 1.2808196544647217 \
   VN: 540 --> NO PATH \

4. Normal: -->  Path length: 362.88692665140957 Planning time: 1.6330735683441162 Edges evaluated: 23016 \
   Lazy: --> Path length: 362.88692665140957 Planning time: 0.2824387550354004 Edges evaluated: 833   \

5. Time spent planning as well as plan length for the first plot (before short cut), was -----> (Path length: 12.960450156532826 Planning time: 0.0031371116638183594) 
   The time spent making the short cut as well as the total path length was now ---> (Shortcut length: 12.591492106547538    Shortcut time: 0.025664329528808594)

6. \
   ![](./map1_curve15.png)  
   ![](./map1_curve3.png) 
   ![](./map1_curve4_5.png)  
   ![](./map1_curve9.png)\
   As the values got higher and higher, the paths ended up having sharper and sharper turns in the name of efficiency. The lowest value of 3 had a big loop for the car to turn on,
   wheras the at 15 there was extremely sharp turns that were even hidden by the vertex.

7. Radius = L / tan(Delta)
   Radius = 0.33 / tan(0.34) = 0.932869
   Curvautre = 1 / Radius
   Curvature = 1.0719

8. \
![](./maze_0_sim_drive.jpg)
	Same parameters as given, (num_vertices:=1000 connection_radius:=10 curvature:=1)


9. \
![](./cse2_2_sim_drive.jpg)
	Parameters, (num_vertices:=1500 connection_radius:=10 curvature:=0.5 initial_x:=16 initial_y:=28)

10. There was no need to change parameters for particle filter and MPC in simulation, but for the real car we needed to tweak particle filter parameters
because while turning the laser scans would get out of synch with the shape of the room. This was mainly reducing the vel_std in motion_parameters

11. See video titled real_car_drive.MOV in the writeup directory
