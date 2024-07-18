
from dataclasses import KW_ONLY
import attrs
from .vectors import Vector


@attrs.define
class CelestialBody():
    name: str = attrs.field(
        default=None,
        kw_only=True,
        metadata={"description": "The name of the celestial body"},
        validator=attrs.validators.instance_of(str)
    )
    mass: float = attrs.field(
        default=None,
        kw_only=True,
        metadata={"description": "The mass of the celestial body in kg"},
        validator=(attrs.validators.instance_of(float), attrs.validators.gt(0))
    )
    position: Vector = attrs.field(
        default=None,
        kw_only=True,
        metadata={"description": "The position of the celestial body as a Vector in meters"},
        validator=attrs.validators.instance_of(Vector)
    )
    velocity: Vector = attrs.field(
        default=None,
        kw_only=True,
        metadata={"description": "The velocity of the celestial body as a Vector in m/s"},
        validator=attrs.validators.instance_of(Vector)
    )
    radius: float = attrs.field(
        default=None,
        kw_only=True,
        metadata={"description": "The radius of the celestial body in meters"},
        validator=(attrs.validators.instance_of(float), attrs.validators.gt(0))
    )