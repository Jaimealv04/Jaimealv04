using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class proyectil : MonoBehaviour {
	public float velocidad;
	// Use this for initialization
	void Start () {
		velocidad = 1;
	}
	
	// Update is called once per frame
	void Update () {

		this.transform.Translate (-1,0,0);
		
	}
}
