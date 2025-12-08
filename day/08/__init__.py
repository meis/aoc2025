from dataclasses import dataclass
import math
from typing import Optional, Tuple


@dataclass
class Point3D:
    x: int
    y: int
    z: int


def part1(input):
    points = _parse_points(input)
    limit = 10 if len(input) < 100 else 1000
    (clusters, _, _) = _get_clusters(points, limit)
    clusters = sorted(clusters, key=lambda x: -len(x))

    return len(clusters[0]) * len(clusters[1]) * len(clusters[2])


def part2(input):
    points = _parse_points(input)
    (_, p1, p2) = _get_clusters(points)

    return p1.x * p2.x


def _get_clusters(points, limit: Optional[int] = None):
    distances = _point_distances(points)

    clusters = [[p] for p in points]
    connections = 0
    for pair in distances:
        connections += 1
        (_, p1, p2) = pair

        cluster1 = None
        cluster2 = None
        for cluster in clusters:
            if p1 in cluster:
                cluster1 = cluster
            if p2 in cluster:
                cluster2 = cluster

        if cluster1 != cluster2:
            clusters.remove(cluster1)
            clusters.remove(cluster2)
            clusters.append(cluster1 + cluster2)

        if connections == limit:
            break

        if len(clusters) == 1:
            break

    return clusters, p1, p2


def _parse_points(input):
    points = []

    for i in input:
        coords = i.split(",")
        points.append(Point3D(int(coords[0]), int(coords[1]), int(coords[2])))

    return points


def _euclidean_distance(p1: Point3D, p2: Point3D) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def _point_distances(points: list[Point3D]) -> list[Tuple[float, Point3D, Point3D]]:
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append(
                (
                    _euclidean_distance(points[i], points[j]),
                    points[i],
                    points[j],
                )
            )

    return sorted(distances, key=lambda x: x[0])
