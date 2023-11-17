using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class camaraReajustada : MonoBehaviour {

	public GameObject Personaje;
	private Vector3 distancia;
	float x;
	float y;
	float z;
	float camX;
	float camY;
	float camZ;
	// Use this for initialization
	void Start () {		
		distancia = this.transform.position - Personaje.transform.position;
		camX = 10.00f;
	}
	
	// Update is called once per frame
	void Update () {
		//limites horizontales
		if (Personaje.transform.position.z >11.0f) {
			camZ = 11.0f;

		} else if (Personaje.transform.position.z < -11.0f) {
			camZ = -11.0f;
		} else {
			camZ = Personaje.transform.position.z;
		}

		//límites verticales

		if (Personaje.transform.position.y > 5.7f) {
			camY = 5.77f;

		} else if (Personaje.transform.position.y < -5.77f) {
			camY = -5.77f;
		} else {
			camY = Personaje.transform.position.y;
		}

		this.transform.position = new Vector3(camX,camY,camZ);

	}



	//new Vector3 (x,y,10.43f)

}